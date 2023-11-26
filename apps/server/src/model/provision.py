from enum import Enum
from pydantic import BaseModel


# Games to Docker Image
class GameType(str, Enum):
    MINECRAFT_JAVA = "itzg/minecraft-server"
    MINECRAFT_BEDROCK = "itzg/minecraft-bedrock-server"


# Server Plans to Server Spec ID
class PlanType(str, Enum):
    LIGHT = "vhp-1c-1gb-amd"
    BASIC = "voc-g-1c-4gb-30s-amd"
    PREMIUM = "voc-m-1c-8gb-50s-amd"


class CreateServer(BaseModel):
    game_type: GameType
    plan_type: PlanType
