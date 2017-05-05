import requests
import os

def create_path(n):
    """Create the path for retrieving Jpeg from."""
    return 'http://www.nhm.ac.uk/resources/visit/wpy/2016/large/{}.jpg'.format(n)


def get_jpg(path):
    """Download the jpeg from website. Return the jpeg and status code."""
    print(path)
    result = requests.get(path, stream=True)
    return result, result.status_code


def save_jpg(response, n):
    """Save the jpeg file to disk."""
    path = '{}.jpeg'.format(n)
    with open(path, 'wb') as f:
        for chunk in response:
            f.write(chunk)

def file_exists(n):
    """Check whether the file already exists before downloading."""
    path = '{}.jpeg'.format(n)
    return os.path.exists(path)


def main():
    for n in range(1, 1000):
        try:
            path = create_path(n)
            if file_exists(n):
                # Don't re-download files that already exist.
                continue

            content, status_code = get_jpg(path)
            if status_code == 404:
                # if we get 404 then break out the loop to avoid DDOS'ing.
                break
            else:
                save_jpg(content, n)
        except:
            break


if __name__ == '__main__':
    main()

