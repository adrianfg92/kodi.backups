# from mega import Mega
#
# FOLDERNAME = 'Kodi'
# FAVOURITES = 'favourites.xml'
#
# mega = Mega()
# m = mega.login(username, password)
#
# # Get folder andcreate folder if not exist
# folder = m.find(FOLDERNAME)
# if not folder:
#     m.create_folder(FOLDERNAME)
#     folder = m.find(FOLDERNAME)
#
# # Deleting old backup
# file = m.find(FAVOURITES)
# if file:
#     m.destroy(file[0])
#
# # Upload new backup
# m.upload(FAVOURITES, folder[0])
