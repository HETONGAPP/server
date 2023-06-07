import websockets
import asyncio
import os
import setproctitle
import argparse

async def file_transfer(websocket, path):

    zipfile_name = args.zipfile_name
    zipfile = "/home/khadas/ivero_results/" + zipfile_name

    if zipfile:
        file_size = os.path.getsize(zipfile)
        file_name = os.path.basename(zipfile)
        # Send the file name and file size to the client
        await websocket.send(f"{file_name}:{file_size}")
        # Open the file and send its contents in chunks
        with open(zipfile, 'rb') as file:
            while True:
                chunk = file.read(1024*1024*10)  # Read 1KB at a time
                if not chunk:
                    break
                await websocket.send(chunk)

    await websocket.close()


async def run_server():
    server = await start_server
    print('Server started')

    # Wait for the file transfer to complete
    await server.wait_closed()
    print('File transfer completed. Exiting.')

    # Stop the event loop after file transfer is complete
    asyncio.get_event_loop().stop()

# Run the server until the file transfer is complete

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="get the zip file name to download.")
    parser.add_argument("zipfile_name", type=str, help="Name of the zip file to download")
    args = parser.parse_args()
    start_server = websockets.serve(file_transfer, '', 8765)
    setproctitle.setproctitle("FileSender")
    asyncio.get_event_loop().run_until_complete(run_server())
