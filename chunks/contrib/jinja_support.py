from jinja2 import Markup
from ..templatetags.chunks import ChunkNode, GetChunkNode


def chunk(key, cache_time=0, *args, **kwargs):
    content = ChunkNode(key, cache_time).render({})
    return Markup(content)


def get_chunk(key, *args, **kwargs):
    return GetChunkNode(key, None).get_chunk()


def context_processor(request):
    out = dict()
    out[chunk.__name__] = chunk
    out[get_chunk.__name__] = get_chunk
    return out
