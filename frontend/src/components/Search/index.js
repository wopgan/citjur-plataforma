import "./search.css"

function SearchBox() {
    return(
        <div className="bg-main">
           
            <div className="searchBox">


                <div className="findUperBox">
                    <input className="findBox" placeholder="Busacar citação" type="text" />

                    <button className="btn-find">

                        <i class="fa-sharp fa-solid fa-magnifying-glass"></i>

                    </button>
                </div>

            </div>


        </div>
    );
}

export default SearchBox;