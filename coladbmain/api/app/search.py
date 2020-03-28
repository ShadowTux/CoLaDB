# search function script

from flask import current_app

# indexing entries for search
def add_to_index(index, model):
  if not current_app.elasticsearch:
    return
  payload = {}
  for field in model.__searchable__:
    payload[field] = getattr(model, field)
  current_app.elasticsearch.index(index=index, id=model.id, body=payload)

# removing entries from index if they're deleted from the db
def remove_from_index(index, model):
  if not current_app.elasticsearch:
    return
  current_app.elasticsearch.delete(index=index, id=model.id)

# actual search query
def query_index(index, query, page, per_page):
  if not current_app.elasticsearch: # this so in case elasticsearch isn't configured, app will work without issues
    return [], 0
  search = current_app.elasticsearch.search(
    index=index,
    body={'query': {'multi_match': {'query': query, 'fields': ['*']}},
    'from': (page - 1)*per_page, 'size': per_page})
  ids = [int(hit['_id']) for hit in search['hits']['hits']]
  return ids, search['hits']['total']['value']