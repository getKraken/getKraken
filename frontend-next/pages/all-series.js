import NavBar from '../components/NavBar';
import SeriesListForm from '../forms/SeriesListForm';
import axios from 'axios';

export default function AllSeries(props) {

  return (
    <div className="SeriesListPage">
      <NavBar />
      <SeriesListForm seriesData={props.seriesData} />
    </div>
  )
}

async function loginAndFetch() {

  let url = "https://get-kraken.herokuapp.com/api/v1/token/";

  // DANGER: hard coded user for moment
  const username = "superuser";
  const password = "uncommon";
  const response = await axios.post(url, { username, password });

  url = 'http://get-kraken.herokuapp.com/api/v1/series';

  let JWTToken = response.data.access;
  let config = { headers: { "Authorization": `Bearer ${JWTToken}` } };

  try {

    let response = await axios.get(url, config);
    return response.data;

  } catch (e) {
    console.error("Excessive token failure")
  }
}

export async function getServerSideProps() {
  const seriesData = await loginAndFetch();
  return {
    props: { seriesData },
  }
}