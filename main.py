import requests
def download(idArtWorks:str) -> None:
    headers = {
        'authority': 'api.pixai.art',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'content-type': 'application/json',
        'origin': 'https://pixai.art',
        'referer': 'https://pixai.art/',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    }

    json_data = {
        'query': '\n    query getArtwork($id: ID!) {\n  artwork(id: $id) {\n    ...ArtworkBase\n  }\n}\n    \n    fragment ArtworkBase on Artwork {\n  __typename\n  id\n  title\n  authorId\n  authorName\n  author {\n    ...UserBase\n  }\n  mediaId\n  prompts\n  createdAt\n  updatedAt\n  media {\n    ...MediaBase\n  }\n  isNsfw\n  hidePrompts\n  isPrivate\n  tags {\n    ...TagBase\n  }\n  extra\n  likedCount\n  liked\n  views\n  commentCount\n  inspiredCount\n  deriveThemeId\n  rootThemeId\n}\n    \n\n    fragment UserBase on User {\n  id\n  email\n  emailVerified\n  username\n  displayName\n  createdAt\n  updatedAt\n  avatarMedia {\n    ...MediaBase\n  }\n  followedByMe\n  followingMe\n  followerCount\n  followingCount\n  inspiredCount\n  isAdmin\n  isGuest\n}\n    \n\n    fragment MediaBase on Media {\n  id\n  type\n  width\n  height\n  urls {\n    variant\n    url\n  }\n  imageType\n  fileUrl\n  duration\n  thumbnailUrl\n  hlsUrl\n  size\n}\n    \n\n    fragment TagBase on Tag {\n  id\n  name\n  mediaId\n  media {\n    ...MediaBase\n  }\n  category\n  weight\n  rootTagId\n  createdAt\n  updatedAt\n  extra\n}\n    ',
        'variables': {
            'id': idArtWorks,
        },
    }
    try:
        urlImgPublic = requests.post('https://api.pixai.art/graphql', headers=headers, json=json_data).json()['data']['artwork']['media']['urls'][0]['url']# variant: "PUBLIC"
        rawImage = requests.get(urlImgPublic).content
        fileName=f"{idArtWorks}.png"
        with open(fileName,'wb+') as f:
            f.write(rawImage)
            f.close()
        print("Download success ",fileName)
    except:
        print("Error while get url art !!!!")


download('1635069401939403516')