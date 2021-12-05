import * as React from "react";
import {
    Drawer,
    AppBar,
    Box,
    Toolbar,
    Typography,
    Button,
    IconButton,
    List,
    ListItem,
    ListItemIcon,
    ListItemText,
} from "@mui/material";
import MenuIcon from "@mui/icons-material/Menu";
import InboxIcon from "@mui/icons-material/MoveToInbox";
import MailIcon from "@mui/icons-material/Mail";
import dummy from "../menu/menulist.json"
import { Link } from "react-router-dom";

export default function ButtonAppBar() {
    const [state, setState] = React.useState(false);

    const toggleDrawer = (open) => {
        setState(open);
    };

    return (
        <Box sx={{ flexGrow: 1 }}>
            <AppBar position="static">
                <Toolbar>
                    <IconButton
                        onClick={() => toggleDrawer(true)}
                        size="large"
                        edge="start"
                        color="inherit"
                        sx={{ mr: 2 }}
                    >
                        <MenuIcon />
                    </IconButton>
                    <Drawer open={state} onClose={() => toggleDrawer(false)}>
                        <Box
                            sx={{ width: {
                                xs:500,
                                sm:250,
                            }, }}
                            rolse="presentation"
                            onClick={() => toggleDrawer(false)}
                            onKeyDown={() => toggleDrawer(false)}
                        >
                            <List>
                            <button type="button" className="close_btn" onClose={() => toggleDrawer(false)}>닫기</button>
                                {dummy.menus.map((menu, index) => (
                                    <ListItem
                                        button
                                        component={Link}
                                        to={`/${menu.id}`}
                                        key={menu.id}
                                        tabindex={index}
                                    >
                                        <ListItemIcon>
                                            {index % 2 === 0 ? (
                                                <InboxIcon />
                                            ) : (
                                                <MailIcon />
                                            )}
                                        </ListItemIcon>
                                        <ListItemText>{menu.menu}</ListItemText>
                                    </ListItem>
                                ))}
                                
                            </List>
                        </Box>
                    </Drawer>
                    <Typography
                        variant="h6"
                        component="div"
                        sx={{ flexGrow: 1 }}
                    >
                        Menu
                    </Typography>
                    <Button color="inherit" component={Link} to="Login">Login</Button>
                </Toolbar>
            </AppBar>
        </Box>
    );
}
