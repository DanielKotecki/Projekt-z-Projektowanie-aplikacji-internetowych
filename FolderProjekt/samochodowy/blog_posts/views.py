from flask import render_template,url_for,request,redirect,Blueprint
from flask_login    import current_user,login_required
from samochodowy import db
from samochodowy.models import BlogPost
from samochodowy.blog_posts.forms import BlogPostForm

blog_posts=Blueprint('blog_posts',__name__)

#Tworzenie posta 
@blog_posts.route('/create',methods=['GET','POST'])
@login_required
#tworzenie
def creat_post():
    form=BlogPostForm()
    if form.validate_on_submit():
        post=BlogPost(title=form.title.data,
        text=form.text.data,
        user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('core.index'))
    return render_template('creat.html',form=form)
        

    #widok
@blog_posts.route('/<int:blog_post_id>')
def blog_post(blog_post_id):
    blog_post = BlogPost.query.get_or_404(blog_post_id)
    return render_template('blog_post.html',title=blog_post.title,
                            date=blog_post.date,post=blog_post
    )
@blog_posts.route("/<int:blog_post_id>/delete", methods=['POST'])
@login_required
def delete_post(blog_post_id):
    blog_post = BlogPost.query.get_or_404(blog_post_id)
    if blog_post.author != current_user:
        abort(403)
    db.session.delete(blog_post)
    db.session.commit()
    return redirect(url_for('core.index'))
