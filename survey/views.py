from django.http import JsonResponse
from django.shortcuts import render
from PIL import Image
import glob
from image_tagger import settings
from survey.models import Survey
import random

image_list = []

# Create your views here.

def index(request):
    #profile = Profile.objects.get(user_id=request.user.id)
    #user = User.objects.get(username=request.user)
    pth =settings.MEDIA_ROOT+'/ILSVRC2013_train_extra0/*.JPEG'
    print(pth)
    all_images = []
    for filename in glob.glob(pth):  # assuming gif
        print(filename)
        #all_images.append(filename.rsplit('/', 2)[1]+"/"+filename.rsplit('/', 2)[2])
        all_images.append( (filename.rsplit('/', 2)[2]).replace('\\', '/'))
        #im = Image.open(filename)
        #image_list.append(im)

    ret_images = []
    print(all_images.__len__())
    for img in all_images:
        """
        decis = random.randint(0,1)
        if decis == 1:
            ret_images.append(img)
        """
        ret_images.append(img)
    #print(all_images)
    print(ret_images[0])

    return render(request, 'survey/index.html', {'images':ret_images})

def poll(request):
    #pth= request.get_full_path().split('/')[:-2]
    #req_url = "http://"+request.get_host()+"/"+pth[1]+"/"+pth[2]+"/"
    #req_url = pth[1]+"/"+pth[2]
    #print()
    #print(pth)
    coms = [{ "parents":"", "children":""}]
    print(request.POST)
    if request.method == "POST":
        #book = get_object_or_404(Book, slug=slug)
        sur = Survey.objects.create( labeled_by=request.POST['author'], image_path=request.POST['image'], label=int(request.POST['label']))
        #sur.
        sur.save()
        print(request.POST['author'])
    #    coms = get_comments(req_url)
        #print(coms)
    return JsonResponse(coms, safe=False)