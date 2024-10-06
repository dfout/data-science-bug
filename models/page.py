class PagePermCheckMixin:
  """
  Check that the user has permission to access the page.
  """

  def __init__(self):
    self.page_id = None

  def dispatch(self, request, *args, **kwargs):
    try:
      decoded_auth_code: dict = signing.loads(request.COOKIES.get('pd_auth_code'))
    except signing.BadSignature:
      return JsonResponse(
        {'detail': 'Missing token'}, status=status.HTTP_403_FORBIDDEN
      )

    self.page_id = kwargs.get('page_id', None)
    if not self.page_id:
      return JsonResponse(
        {'detail': 'No page_id provided.'}, status=status.HTTP_403_FORBIDDEN
      )

    user_id = decoded_auth_code["user_id"]

    is_permitted = models.Page.objects.filter(id=self.page_id, project__user_id=user_id).exists()
    if not is_permitted:
      return JsonResponse(
        {'detail': 'You haven\'t provided the correct credentials to access this.'},
        status=status.HTTP_403_FORBIDDEN
      )

    return super().dispatch(request, *args, **kwargs)