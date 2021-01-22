import SeriesList from '../forms/SeriesListForm';
import NavBar from '../components/NavBar';
import SingleSeriesForm from '../forms/SingleSeriesForm'
import SeriesListForm from '../Forms/SeriesListForm';

export default function AllSeries(){

  return(
    <div className="SeriesListPage">
      <NavBar/>
      <SeriesListForm/>
    </div>  
  )
}