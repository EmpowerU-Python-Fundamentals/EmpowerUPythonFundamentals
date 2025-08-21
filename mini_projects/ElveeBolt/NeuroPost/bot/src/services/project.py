from datetime import datetime, timedelta, timezone

from sqlalchemy import select, and_, update
from sqlalchemy.orm import selectinload

from src.database import get_session
from src.models import Project, ProjectPlan, ProjectPlanPost


async def get_posts():
    async with get_session() as session:
        now = datetime.now(timezone.utc).replace(second=0, microsecond=0)
        next_minute = now + timedelta(seconds=60)

        stmt = (
            select(ProjectPlanPost)
            .options(
                selectinload(ProjectPlanPost.plan).selectinload(ProjectPlan.project)
            )
            .where(
                and_(
                    ProjectPlanPost.is_draft == False,
                    ProjectPlanPost.is_published == False,
                    ProjectPlanPost.is_approved == True,
                    ProjectPlanPost.publish_at >= now,
                    ProjectPlanPost.publish_at < next_minute,
                )
            )
        )
        result = await session.execute(stmt)
        return result.scalars().all()


async def update_post_publish_status(post_id: int):
    async with get_session() as session:
        stmt = (
            update(ProjectPlanPost)
            .where(ProjectPlanPost.id == post_id)
            .values(is_published=True)
        )
        await session.execute(stmt)
        await session.commit()
