import SeriesList from '../forms/SeriesListForm';
import NavBar from '../components/NavBar';
import SingleSeriesForm from '../forms/SingleSeriesForm'

export default function AllSeries(){
  // These props are coming from the API call to the fetch the series data
  const userData = {
    'username' : 'yoni',
  }
  const allSeries = [
    {'id': 1, 'title':'kraken-season-2021', 'organizer':'paul','participants':['yoni','paul','will','mark']},
    {'id': 2, 'title':'shabbat-winter-2021', 'organizer':'yoni','participants':['yoni','paul','will','mark']},
    {'id': 3, 'title':'operah-winter-2021', 'organizer':'will','participants':['yoni','paul','will','mark']},
    {'id': 4, 'title':'seahawks-season-2021', 'organizer':'mark','participants':['yoni','paul','will','mark']},
  ]
  return(
    <div className="SeriesListPage">
      <NavBar/>
      <p>Welcome {userData.username}!</p>

      <h2> Series</h2>
      <SeriesList allSeries={allSeries}></SeriesList>
      <SingleSeriesForm/>
    </div>  
  )
}