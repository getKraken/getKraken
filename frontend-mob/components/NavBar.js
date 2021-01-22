export default function NavBar(props) {
    return (
      <header className='bg-red-600'>
      <ul class='flex flex-row place-content-between'>
        <li> <a href='../all-series'><img class='ml-4 mt-4 w-64 h-64' src='https://i.pinimg.com/originals/8d/e7/2b/8de72ba1f8a9bcf1ec9edc1184236565.jpg'/></a> </li>
    
        <li class='mt-32'> <strong class='font-extrabold text-6xl'>GetKraken</strong> </li>
    
        <li class='h-12 mt-32 bg-blue-400 px-4 py-2 rounded hover:bg-blue-200'><a href='../new-series'>New Series</a></li>
    
        <li class= 'h-12 mr-4 mt-32 bg-blue-400 px-4 py-2 rounded hover:bg-blue-200'><a href='/'> Logout </a></li>
      </ul>
    </header>
    );
}