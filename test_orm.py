import recommendations
from datetime import date


def test_item_table_can_load_lines(session):
    session.execute(
        "INSERT INTO items (Name) VALUES "
        '("cookies"),'
        '("beer")'
    )
    expected = [
        recommendations.Item("cookies"),
        recommendations.Item("beer"),
    ]
    assert session.query(recommendations.Item).all() == expected


def test_user_table_can_load_lines(session):
    session.execute(
        "INSERT INTO users (userName) VALUES "
        '("EddieEats"),'
        '("DominicDrinks")'
    )
    expected = [
        recommendations.User("EddieEats"),
        recommendations.User("DominicDrinks"),
    ]
    assert session.query(recommendations.User).all() == expected


def test_recommendations_table_can_load_lines(session):
    session.execute(
        "INSERT INTO recommendations (date, matchid, itemID, url) VALUES "
        '("2020-7-25", "Shell-Silver", "cookies", "www.findyouritem.com"),'
        '("2020-2-2", "Shell-Tina", "cookies", "www.findyourcookie.com")'
    )
    expected = [
        recommendations.Recommendation(
            "Shell-Silver", "cookies", "www.findyouritem.com", date=date(2020,7,25)),
        recommendations.Recommendation(
            "Shell-Tina", "cookies", "www.findyourcookie.com",date=date(2020,2,2)),
    ]
    assert session.query(recommendations.Recommendation).all() == expected



