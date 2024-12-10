from django.shortcuts import render

class Stories:
    def __init__(self, name, description, story, tags, photo):
        self.name = name,
        self.description = description,
        self.story = story,
        self.tags = tags,
        self.photo = photo,

stories = [
    Stories('name', 'description', 'story', 'tags', 'photo url'),
    Stories('Far from her', 'A world where I am away from her', 'Once a upon... the end', 'romance', 'url.com'),
    Stories('A cup', 'A story about a blue cup', 'The cup was gray and it is blue. The end', 'comedy', 'url.com' ),
    Stories('good guy', 'he once was a bad guy', 'He was evil but now turned to good', 'superhero', 'photourl.com')
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def story_index(request):
    return render(request, 'story/index.html', {'stories': stories})