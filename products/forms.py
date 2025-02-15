from django import forms
from .models import ProductImage
######### class ProductImageForm(forms.ModelForm):
    ##########this will return only first saved image on save()
      image = forms.ImageField(widget=forms.FileInput(attrs={'multiple': True}), required=True)
 
    class Meta:
        model = ProductImage
        fields = ['image', 'scale','product']

    def save(self, *args, **kwargs):
        #########multiple file upload
        #########NB: does not respect 'commit' kwarg
        #########file_list = natsorted(self.files.getlist('{}-image'.format(self.prefix)), key=lambda file: file.name)

        self.instance.image = file_list[0]
        for file in file_list[1:]:
            ProductImage.objects.create(
                product=self.cleaned_data['product'],
                image=file,
                scale=self.cleaned_data['scale'],
            )

        return super().save(*args, **kwargs)
        
# class ProductImageForm(forms.ModelForm):
    # class Meta:
        # model = ProductImage
        # fields = ['image', 'scale','product']