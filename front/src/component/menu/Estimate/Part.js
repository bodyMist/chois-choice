export default function Part({ component_id, image_url, name, selectPart, key }) {
    const getPart = (e) => {
        const component_id = e.target.id;
        selectPart(component_id);
    };
    return (
        <tr>
            <td className="StuffIcon">
                <img alt="1" src={image_url} />
            </td>
            <td className="btn" id={component_id} onClick={getPart} key={key} >
                {name}
            </td>
        </tr>
    );
}
