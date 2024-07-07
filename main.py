from ytmusicapi import YTMusic
import pandas as pd
import os

# Initialize YTMusic
# oauth.json file needs to be created beforehand, doc: https://ytmusicapi.readthedocs.io/en/stable/setup/oauth.html
ytmusic = YTMusic('oauth.json')

csv_locations = input('Folder containing CSV files: ')

# Loop over all files in the directory
for filename in os.listdir(csv_locations):
    # Check if the file is a CSV file
    if filename.endswith(".csv"):
        # Construct the full file path
        filepath = os.path.join(csv_locations, filename)
        # Read the CSV file into a pandas DataFrame
        data = pd.read_csv(filepath)

        # Playlist creation
        playlistName = os.path.splitext(filename)[0]
        playlistDescription = ''  # unused
        playlistId = ytmusic.create_playlist(playlistName, playlistDescription)

        print(f'Creating playlist called {playlistName}...')

        # YouTube queries by Title and Artist
        for i in range(data.shape[0]):
            try:
                search_results = ytmusic.search(data.loc[i, 'Title'] + " " + data.loc[i, 'Artist'], 'songs', None,
                                                1)  # Change the filter to None to allow videos - can be useful
                if search_results:
                    ytmusic.add_playlist_items(playlistId, [search_results[0]['videoId']])
                    print(f'Added song {data.loc[i, "Title"]} by {data.loc[i, "Artist"]} to playlist {playlistName}.')
                else:
                    print(f'No results found for song {data.loc[i, "Title"]} by {data.loc[i, "Artist"]}.')
            except Exception as e:
                print(f'An error occurred while adding song {data.loc[i, "Title"]} by {data.loc[i, "Artist"]} to '
                      f'playlist {playlistName}: {str(e)}')

        print(f'{playlistName} created.')
