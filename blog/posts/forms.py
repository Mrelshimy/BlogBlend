from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField


class CreateAndUpdatePostForm(FlaskForm):
    """
    A form for creating and updating posts.
    """
    title = StringField('Title',
                        render_kw={'placeholder': 'title of the post'})
    content = TextAreaField('Content',
                            render_kw={'placeholder': 'content of the post'})
    # tags = StringField('Tags',
    # render_kw={'placeholder': 'space-separated tags'})
    post_image = FileField('Post Image',
                           validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Post')

# class CommentForm(FlaskForm):
#     content = TextAreaField('Content', validators=[DataRequired()],
#     render_kw={'placeholder': 'content of the comment'})
#     submit = SubmitField('Comment')


# class LikeForm(FlaskForm):
#     post_id = HiddenField()
#     submit = SubmitField('Like')
