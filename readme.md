# city voice

to do

- [ ] accounts
    - [x] general `is_expert = False`
    - [x] expert/govt `is_expert = True`
    - [x] login : `/user/login/`
        - [x] username
        - [x] password
        - [ ] else : 
            - [ ] phone
                - [ ] otp
                - [x] phone and password? `username = User.objects.get(phone=phone)`
    - [x] register : `/user/register`
        - [x] username
        - [x] password
        - [x] phone
    - [x] logout `/user/logout`
- [x] profile page `/user/<username>`
    - [x] follow `/user/<username>/follow`
    - [x] unfollow `/user/<username>/unfollow`
    - [x] followers list
    - [x] following list
- [ ] post creation `/post/new`
    - [x]  text
    - [ ]  image
    - [ ]  video
- [ ] tag other accounts in post
- [ ] reply to post
- [x] upvote downvote posts
- [x] upvote downvote replys
- [x] hashtags ( topics ) `labels`
- [ ] search and filters
    - [x] search by user? `/user/<username>/posts`
- [ ] notifications
- [ ] talk with other servers