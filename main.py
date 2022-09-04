from instagrapi import Client
from os import getenv


def insta_auth():
    USERNAME = getenv('LOGIN')
    PASSWORD = getenv('PASSWORD')
    
    try:
        cl = Client()
        cl.login(USERNAME, PASSWORD)
        
        return cl
    except Exception as ex:
        print(ex)
        print('Something Was Wrong :(')
        
        
def get_user_medias(cl, username='miami'):
    user_id = cl.user_id_from_username(username)
    medias = cl.user_medias(user_id, 5)
    
    # for item in medias[:1]:
    #     # print(item, '\n')
    #     # print(item.pk)
        
    #     cl.video_download(media_pk=item.pk, folder='path_to_media_folder')
    
    cl.photo_download(media_pk='item_pk', folder='path_to_media_folder')
    

def media_like(cl, username='miami'):
    user_id = cl.user_id_from_username(username)
    # cl.media_like(media_id=f'media_id_{user_id}')
    cl.media_unlike(media_id=f'media_id_{user_id}')


def main():
    cl = insta_auth()
    # get_user_medias(cl)
    media_like(cl)
    
    
if __name__ == '__main__':
    main()
