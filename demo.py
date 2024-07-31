import urllib.request as request
def download_file():
        

        response = request.urlopen("https://raw.githubusercontent.com/Balkrishna1Tiwari/Name_Entity_Recognition2/main/dataset.zip")
        content_type = response.info().get('Content-Type')
        if 'zip' in content_type:
            with open('data32.zip', 'wb') as out_file:
                out_file.write(response.read())
                    # logger.info(f"{self.data_ingestion_config.ZIP_FILE_PATH} downloaded successfully.")
                
download_file()