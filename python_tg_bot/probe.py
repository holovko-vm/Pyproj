def kill(args, update: Update, context: CallbackContext) -> None:
    for _ in args:
        update.message.reply_text(f'We kill {_}')