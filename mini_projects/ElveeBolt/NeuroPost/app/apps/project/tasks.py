from celery import shared_task
from .models import ProjectPlan, ProjectPlanPost
from .services.Agent.Agent import PlanAgent, PostAgent
from .services.Agent.PromptBuilder import PlanPromptBuilder, PostPromptBuilder


@shared_task
def create_project_plan(plan_id):
    plan = ProjectPlan.objects.get(id=plan_id)
    prompt = PlanPromptBuilder().build(
        project_title=plan.project.title,
        plan_description=plan.description,
        plan_count_post=plan.post_count
    )
    posts = PlanAgent().create_response(prompt=prompt)


    for post in posts:
        generate_project_post.delay(plan_id=plan_id, post_title=post)

    return plan.id


@shared_task
def generate_project_post(plan_id: int, post_title: str):
    plan = ProjectPlan.objects.get(id=plan_id)
    prompt = PostPromptBuilder().build(
        project_title=plan.project.title,
        post_title=post_title,
        max_symbols=plan.max_symbols,
    )
    print(prompt)
    post = PostAgent().create_response(prompt=prompt)

    obj = ProjectPlanPost.objects.create(
        plan=plan,
        title=post_title,
        description=post
    )

