export default function NavBar(props) {
    return (
        <header>
          <ul>
            <li> <a href='../series-list'><img src='http://placekitten.com/200/300'/></a> </li>

            <li> GetKraken </li>

            <li><a href='../new-series'>Create a Series</a></li>

            <li><a href='/'> Logout Button </a></li>
          </ul>
        </header>
    );
}