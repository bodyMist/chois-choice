import PartSelect from "./PartSelect";
import PartSelected from "./PartSelected";

export default function PcEstimate() {
    return (
        <div className="container-pc">
            <PartSelect/>
            <PartSelected/>
        </div>
    );
}