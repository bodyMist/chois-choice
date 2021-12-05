export default function Part({ list, selectPart, key }) {
    const getPart = (e) => {
        const component_id = e.target.id;
        selectPart(component_id);
    };
    return (
        <tr>
            <td className="StuffIcon">
                <img alt="1" src={list.image_url} />
            </td>
            <td className="btn" id={list.component_id} onClick={getPart} key={key} >
                {list.name}
            </td>
        </tr>
    );
}
