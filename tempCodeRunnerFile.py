db.drop_all()
        db.create_all()
        return redirect(url_for("test"))