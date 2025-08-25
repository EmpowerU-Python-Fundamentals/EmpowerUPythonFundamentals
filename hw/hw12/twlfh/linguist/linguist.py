from card import card_update, card_create, card_filter, card_get_by_id, card_delete_by_id
from user import user_create, user_get_by_id, user_delete_by_id, user_update_name, user_change_password
from deck import deck_create, deck_update, deck_get_by_id, deck_delete_by_id


u1 = user_create('Vitalii', 'mail@mail.com', 'qwerty')
assert u1.name == 'Vitalii'
assert u1.email == 'mail@mail.com'

d1 = deck_create('fruit', u1.id)
assert d1.name == 'fruit'
assert d1.user_id == u1.id

c1 = card_create(u1.id, 'apple', 'яблуко', 'juice')
assert c1.word == 'apple'
assert c1.translation == 'яблуко'
assert c1.tip == 'juice'

retrieved_user = user_get_by_id(u1.id)
assert retrieved_user.name == 'Vitalii'

filtered_cards = card_filter('apple')
assert len(filtered_cards) == 1
assert filtered_cards[0].word == 'apple'

updated_user = user_update_name(u1.id, 'Vasyl')
assert updated_user.name == 'Vasyl'

password_changed = user_change_password(u1.id, 'qwerty', 'qwerty111')
assert password_changed is True

update_card = card_update(c1.card_id, 'watermelon', 'кавун', 'berry')
assert update_card.word == 'watermelon'
assert update_card.translation == 'кавун'
assert update_card.tip == 'berry'

get_card = card_get_by_id(c1.card_id)
assert get_card.card_id == c1.card_id

get_deck = deck_get_by_id(d1.deck_id)
assert get_deck.deck_id == d1.deck_id

update_deck = deck_update(d1.deck_id, 'my fruit')
assert update_deck.name == 'my fruit'


del_card = card_delete_by_id(c1.card_id)
assert del_card is True
assert card_get_by_id(c1.card_id) is None

del_user = user_delete_by_id(u1.id)
assert del_user is True
assert user_get_by_id(u1.id) is None

del_deck = deck_delete_by_id(d1.deck_id)
assert del_deck is True
assert deck_get_by_id(d1.deck_id) is None








