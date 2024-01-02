from .controllers import *

# Define a list of models
models = [Student, Program, Subjects, Curriculum, Prospectus]

def create_endpoints_for_model(model):
    # Dynamically getting the serializer class based on the model name
    serializer_class = globals()[f"{model.__name__}Serializer"]

    @csrf_exempt
    def list_view(request, pk=None):
        return generic_list(request, model, serializer_class, pk)

    @csrf_exempt
    def filter_view(request):
        return filter_model(request, model, serializer_class)

    @csrf_exempt
    def delete_view(request, pk=None):
        return generic_delete(request, model, pk)

    return list_view, filter_view, delete_view

# Generate endpoints for each model
for model in models:
    list_view, filter_view, delete_view = create_endpoints_for_model(model)
    globals()[f"{model.__name__}_list"] = list_view
    globals()[f"{model.__name__}_filter"] = filter_view
    globals()[f"{model.__name__}_delete"] = delete_view
