from app.config.settings import Settings
from googleapiclient.discovery import build

class DescriptionExtractor:

    def __init__(self):
        self.youtube = build(
            serviceName='youtube',
            version='v3',
            developerKey=Settings.apiKey
        )

    def obter_descricao_video(self, video_id):
        request = self.youtube.videos().list(
            part="snippet",
            id=video_id
        )
        response = request.execute()

        if "items" in response and len(response["items"]) > 0:
            return response["items"][0]["snippet"]["description"]
        else:
            return None