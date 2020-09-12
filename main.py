from instapy import InstaPy, smart_run

from conf import username, password

session = InstaPy(
    username=username,
    password=password,
    headless_browser=True,
)

with smart_run(session):
    session.login()
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=None,
                                    delimit_by_numbers=True,
                                    max_followers=20000,
                                    min_followers=1000,
                                    max_following=2000,
                                    )

    amount_number = 1000

    session.set_do_like(enabled=False, percentage=0)

    session.set_do_comment(enabled=False, percentage=0)

    session.set_do_follow(enabled=False, percentage=0)

    session.follow_user_followers(['karazinuniver'], amount=amount_number, randomize=False, interact=False,
                                  sleep_delay=300)
    # session.set_do_comment(False)
    # session.set_do_like(False)
    # session.set_do_follow(True)
    # followers = session.grab_followers(username='student.nure', amount=5, live_match=False, store_locally=False)

    # print(followers)