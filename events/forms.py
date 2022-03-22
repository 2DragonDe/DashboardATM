from django import forms
from bootstrap_modal_forms.forms import BSModalForm, BSModalModelForm
from events.models import Event, Comment

class EventForm(BSModalModelForm):
    class Meta:
        model = Event
        exclude = ('author',)
        fields = '__all__'
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control selectpicker', 'data-style': 'btn btn-rose btn-sm', 'placeholder': 'Trạng Thái Sự Kiện'}),
            'status_atm': forms.Select(attrs={'class': 'form-control selectpicker', 'data-style': 'btn btn-rose btn-sm', 'placeholder': 'Trạng Thái ATM'}),
            'priority': forms.Select(attrs={'class': 'form-control selectpicker', 'data-style': 'btn btn-rose btn-sm', 'placeholder': 'Độ Ưu Tiên'}),
            'author': forms.Select(attrs={'class': 'form-control selectpicker', 'data-style': 'btn btn-rose btn-sm', 'placeholder': 'Người Tạo'}),
            'supervisor_note': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ghi nhận các thông tin ban đầu'}),
            'report24h': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'replace_components': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'end_funds': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'to_funds': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'date_complete': forms.DateTimeInput(format='%m/%d/%Y', attrs={'class':'form-control datetimepicker', 'placeholder': 'Ngày Hoàn Thành'}),
        }

class EventUpdateForm(BSModalModelForm):
    class Meta:
        model = Event
        exclude = ('author', 'name', 'status', 'supervisor_note','date_post' )
        fields = '__all__'
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control selectpicker', 'data-style': 'btn btn-rose btn-sm', 'placeholder': 'Trạng Thái Sự Kiện'}),
            'status_atm': forms.Select(attrs={'class': 'form-control selectpicker', 'data-style': 'btn btn-rose btn-sm', 'placeholder': 'Trạng Thái ATM'}),
            'priority': forms.Select(attrs={'class': 'form-control selectpicker', 'data-style': 'btn btn-rose btn-sm', 'placeholder': 'Độ Ưu Tiên'}),
            'author': forms.Select(attrs={'class': 'form-control selectpicker', 'data-style': 'btn btn-rose btn-sm', 'placeholder': 'Người Tạo'}),
            'report24h': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'replace_components': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'end_funds': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'to_funds': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'date_complete': forms.DateTimeInput(format='%m/%d/%Y %H:%M', attrs={'class':'form-control datetimepicker', 'placeholder': 'Ngày Hoàn Thành'}),
            #'date_post': forms.DateTimeInput(format='%m/%d/%Y', attrs={'class':'form-control datetimepicker', 'placeholder': 'Ngày Post'}),
            'date_close': forms.DateTimeInput(format='%m/%d/%Y %H:%M', attrs={'class':'form-control ', 'placeholder': 'Ngày Kết Thúc', 'value': ''}),
        }
    
    
        
class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label = "",
        required=False,
        widget = forms.Textarea(attrs={'class': 'form-control', 'rows': '1'})
    )
    class Meta:
        model = Comment
        fields = ['content']
        