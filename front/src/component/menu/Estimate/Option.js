import { useState } from "react";

export default function Option({ id, checkedItemHandler, type }) {
    const [bChecked, setChecked] = useState(false);
    const checkedHandler = (e) => {
        setChecked(!bChecked);
        const id = e.target.id

        checkedItemHandler(id, e.target.checked);
    }
    return (
        <>
            
        </>
    );
}