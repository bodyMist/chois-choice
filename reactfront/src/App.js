
import Header from "./component/Header";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import Footer from "./component/Footer";
import Routing from "./Routing";

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
