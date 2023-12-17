from ...src.model.provision import GameType, PlanType, CreateServer


def test_creation():
    game_type = GameType.MINECRAFT_JAVA
    plan_type = PlanType.LIGHT
    create_server = CreateServer(game_type=game_type, plan_type=plan_type)

    assert create_server is not None
