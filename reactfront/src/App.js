
import Header from "./component/Header";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import Footer from "./component/Footer";
import Routing from "./Routing";
import Image from "./component/Image";
import BestPost from "./component/BestPost";

function App() {
    return (
        <BrowserRouter>
            <div className="App">
                <Header />
                <Routing/>
                <Footer/>
            </div>
        </BrowserRouter>
    );
}

export default App;
