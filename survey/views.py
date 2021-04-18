from django.http import JsonResponse
from django.shortcuts import render
from PIL import Image
import glob
from image_tagger import settings
from survey.models import Survey
import random

image_list = []


def index(request):

    # collect all JPEG images
    pth =settings.MEDIA_ROOT+'/ILSVRC2013_train_extra0/*.JPEG'
    #print list of image paths in directory
    print(pth)
    all_images = []
    for filename in glob.glob(pth):  # assuming gif
        all_images.append( (filename.rsplit('/', 2)[2]).replace('\\', '/'))


    ret_images = []
    print(all_images.__len__())
    for img in all_images:

        ret_images.append(img)
    print(ret_images[0])

    return render(request, 'survey/index.html', {'images':ret_images})

def poll(request):

    coms = [{ "parents":"", "children":""}]
    print(request.POST)
    if request.method == "POST":
        #book = get_object_or_404(Book, slug=slug)
        sur = Survey.objects.create( labeled_by=request.POST['author'], image_path=request.POST['image'], label=int(request.POST['label']))
        sur.save()
        print(request.POST['author'])
    #    coms = get_comments(req_url)
        #print(coms)
    return JsonResponse(coms, safe=False)