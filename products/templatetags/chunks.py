from django import template

register=template.Library()

@register.filter(name='chunks')
def chunks(list,chunk_size):
    chunk=[]
    data_count=0
    for data in list:
        chunk.append(data)
        data_count+=1
        if data_count == chunk_size:
            yield chunk
            data_count=0
            chunk=[]
    yield chunk