from .models import Arc



def arcs_list_to_context(request):
    arcs = Arc.objects.all()
    return {
        'arcs': arcs
    }
