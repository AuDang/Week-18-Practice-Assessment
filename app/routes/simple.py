from flask import Blueprint, redirect, render_template
from app.forms import NewInstrument
from app.models import db, Instrument


bp = Blueprint("simple", __name__, url_prefix='/')

@bp.route('/')
def index():
   return render_template("main_page.html")

@bp.route('/new_instrument')
def get_new_instrument():
   form = NewInstrument()
   return render_template("simple_form.html", form=form )

@bp.route('/new_instrument', methods=['POST'])
def submit_new_instrument():
   form = NewInstrument()
   params = {
      "date_bought": form.data['date_bought'],
      'nickname': form.data['nickname'],
      'year':form.data['year'],
      'maker':form.data['maker'],
      'type':form.data['type'],
      'used':form.data['used']
   }

   if form.validate_on_submit():
      instruments = Instrument(**params)

      db.session.add(instruments)
      db.session.commit()
      return redirect('/instrument_data')
   return '<h1>Bad Data</h1>'

@bp.route("/instrument_data")
def instrument_data():
   instrument = Instrument.query.filter(Instrument.nickname.ilike("M%")).all()

   return render_template("simple_form_data.html", instrument = instrument)