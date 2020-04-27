import telegram

from bot.common import Chat, CLUB_CHANNEL, send_telegram_message, render_html_message, send_telegram_image, CLUB_CHAT


def announce_in_club_channel(post, announce_text=None, image=None):
    if not announce_text:
        announce_text = render_html_message("channel_post_announce.html", post=post)

    if image:
        send_telegram_image(
            chat=CLUB_CHANNEL,
            image_url=image,
            text=announce_text,
            parse_mode=telegram.ParseMode.HTML,

        )
    else:
        send_telegram_message(
            chat=CLUB_CHANNEL,
            text=announce_text,
            disable_preview=False,
            parse_mode=telegram.ParseMode.HTML,
        )


def announce_in_club_chat(post):
    send_telegram_message(
        chat=CLUB_CHAT,
        text=render_html_message("channel_post_announce.html", post=post),
        parse_mode=telegram.ParseMode.HTML,
        disable_preview=True,
    )


def notify_post_author_approved(post):
    if post.author.telegram_id:
        send_telegram_message(
            chat=Chat(id=post.author.telegram_id),
            text=render_html_message("post_approved.html", post=post),
            parse_mode=telegram.ParseMode.HTML,
        )


def notify_post_author_rejected(post):
    if post.author.telegram_id:
        send_telegram_message(
            chat=Chat(id=post.author.telegram_id),
            text=render_html_message("post_rejected.html", post=post),
            parse_mode=telegram.ParseMode.HTML,
        )
