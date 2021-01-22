export default function Landing(props) {

    return (

        <section className="text-gray-700 body-font">
            <div className="container px-8 mx-auto pt-36 lg:px-4">
                <div className="flex flex-col w-full mx-auto mb-12 text-left lg:w-2/3 lg:text-center">
                    <h1 className="mb-6 text-2xl font-semibold tracking-tighter text-blue-800 sm:text-5xl title-font">
                        You just wanted to see your friends.
                    </h1>
                    <p className="mx-auto text-base font-medium leading-relaxed text-gray-700 lg:w-2/3">
                    You were the one with the initiative to buy the tickets so everybody could have fun. How did you become the a-hole?
                    </p>
                </div>
                <div className="flex flex-col w-full px-0 mx-auto lg:w-2/3 sm:flex-row md:px-8">
                    <input
                        className="flex-grow w-full px-4 py-2 mb-4 mr-4 text-base text-purple-700 bg-gray-100 border border-gray-400 rounded-lg focus:outline-none focus:border-purple-500 sm:mb-0 focus:bg-white"
                        placeholder="Your Name" type="text" />
                    <input
                        className="flex-grow w-full px-4 py-2 mb-4 mr-4 text-base text-purple-700 bg-gray-100 border border-gray-400 rounded-lg focus:outline-none focus:border-purple-500 sm:mb-0 focus:bg-white"
                        placeholder="Your Password" type="password" />
                    <button
                        className="w-1/2 px-8 py-2 font-semibold text-white transition duration-500 ease-in-out transform rounded-lg shadow-xl bg-gradient-to-r from-blue-700 hover:from-blue-600 to-blue-600 hover:to-blue-700 focus:shadow-outline focus:outline-none">
                            Go
                        </button>
                </div>
                <p className="w-full mt-12 mb-8 text-sm text-center text-gray-500">What are you waiting for Get Kraken!<a href="#"
                        className="inline-flex items-center font-semibold text-blue-700 md:mb-2 lg:mb-0 hover:text-blue-400 ">

                        Sign Up

                        <svg className="w-4 h-4 ml-2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="20"
                            height="20" fill="currentColor">
                            <path fill="none" d="M0 0h24v24H0z" />
                            <path
                                d="M16.172 11l-5.364-5.364 1.414-1.414L20 12l-7.778 7.778-1.414-1.414L16.172 13H4v-2z" />
                        </svg>
                    </a></p>
            </div>
        </section>


    )
}
