import os
from services.configService import ConfigService

env = os.environ.get("FLASK_ENV", "development")
port = os.environ.get("PORT", 8080)

all_environments = ConfigService(env).config

# all_environments = {
#     "development": { "port": 5000, "debug": True, "swagger-url": "/api/swagger" },
#     "production": { "port": port, "debug": False, "swagger-url": None  }
# }
print (all_environments)
environment_config = all_environments
