from ..skeleton import Annotation, AnnoTarget, AnnotationPage, Canvas, ResourceItem
from ..loader import monkeypatch_schema


class AddImageToCanvas:
    def add_image(self, image_url, anno_id, anno_page_id=None):
        body = ResourceItem(id=image_url, type='Image')
        annotation = Annotation(id=anno_id, body=body, target=self.id, motivation='painting', type='Annotation')
        anno_page = AnnotationPage(id=anno_page_id, type='AnnotationPage', items=[annotation])
        if not self.items:
            self.items = list()
        self.items.append(anno_page)
        return anno_page

monkeypatch_schema(Canvas, AddImageToCanvas)
