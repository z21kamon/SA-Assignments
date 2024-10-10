from like_service import LikeService
from post_service import PostService
from user_service import UserService


def main():
    user_service = UserService()
    post_service = PostService()
    like_service = LikeService()

    while True:
        print('1. Register')
        print('2. Post message')
        print('3. View feed')
        print('4. Like message')
        print('5. Exit')
        choice = input('Choose an option: ')

        match choice:
            case '1':
                username = input('Enter a username: ')
                if user_service.user_exists(username):
                    print('Username already taken!')
                    continue
                user_service.sign_up(username)
                print('Registration successful!')
            case '2':
                username = input('Enter your username: ')
                if not user_service.user_exists(username):
                    print('You must be registered to post a message.')
                    continue
                post = input('Enter your message: ')
                print('Message posted!' if post_service.post(username, post) else 'Message too long.')
            case '3':
                feed = post_service.get_feed()
                for id_, author, message, likes_count, time in feed:
                    print(f'[#{id_}] @{author}\n{message}\nLikes: {likes_count}\t\t\t{time}\n-------------------------------')
            case '4':
                post_id = int(input('Enter the #id of the post you want to like: '))
                like_service.like_post(post_id)
                print('Message liked!')
            case '5':
                print('Goodbye!')
                break
            case _:
                print('Invalid option.')

if __name__ == '__main__':
    main()
