import { Link } from "react-router-dom";
import PartSelect from "./PartSelect";
import PartSelected from "./PartSelected";
import PcRecommand from "./PcRecommand";

export default function PcEstimate() {
    return (
        <div className="container">
            {/* <h3>PC 견적</h3> */}
            <Link to="/PcRecommand">견적 추천</Link>
            <div className="container-pc">
                <PartSelect />
                <PartSelected />
            </div>
        </div>
    );
}
