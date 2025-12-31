@Client.on_callback_query(filters.regex("^close$"))
async def close_cb(client, query):
    await query.message.delete()
