import { Link } from "react-router-dom";
import dummy from "../DB/menulist.json";

export default function MenuList() {
    return (
        <ul className="list">
            {dummy.menus.map((menu) => (
                <li key={menu.id}>
                    <Link to={`/${menu.id}`}>{menu.menu}</Link>
                </li>
            ))}
        </ul>
    );
}