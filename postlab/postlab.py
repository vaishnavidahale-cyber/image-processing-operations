import os
import tempfile
import cv2
import numpy as np
import streamlit as st

st.set_page_config(
    page_title="Image Processing Studio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom Styling: Hides Deploy Button, Menu, & Footer; Locks Viewport
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

        * {
            font-family: 'Plus Jakarta Sans', sans-serif;
        }

        /* Screen-fitted viewport padding */
        .block-container {
            padding-top: 4.2rem !important;
            padding-bottom: 1.2rem !important;
            padding-left: 2rem !important;
            padding-right: 2rem !important;
            max-width: 98% !important;
        }

        .stApp {
            background: radial-gradient(circle at 10% 15%, #f8fafc 0%, #f1f5f9 60%, #e2e8f0 100%);
        }

        /* Top Hero Header */
        .hero-banner {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: linear-gradient(135deg, #090d16 0%, #111827 50%, #1e293b 100%);
            border-radius: 14px;
            padding: 14px 24px;
            margin-bottom: 12px;
            box-shadow: 0 10px 25px -8px rgba(15, 23, 42, 0.35);
            border: 1px solid rgba(255, 255, 255, 0.12);
        }
        .main-title {
            font-size: 1.85rem;
            font-weight: 800;
            letter-spacing: -0.8px;
            background: linear-gradient(135deg, #ffffff 0%, #a5b4fc 60%, #818cf8 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin: 0;
            line-height: 1.1;
        }
        .sub-title {
            font-size: 0.82rem;
            color: #94a3b8;
            font-weight: 500;
            margin-top: 2px;
        }

        /* Full Aim Display Card */
        .aim-card {
            background: rgba(255, 255, 255, 0.85);
            backdrop-filter: blur(12px);
            border: 1px solid #e0e7ff;
            border-left: 5px solid #6366f1;
            border-radius: 10px;
            padding: 10px 16px;
            margin-bottom: 14px;
            box-shadow: 0 4px 14px rgba(99, 102, 241, 0.05);
            color: #334155;
            font-size: 0.84rem;
            line-height: 1.45;
        }
        .aim-tag {
            background: #ede9fe;
            color: #6366f1;
            font-weight: 700;
            font-size: 0.72rem;
            padding: 2px 7px;
            border-radius: 4px;
            margin-right: 6px;
            letter-spacing: 0.5px;
            text-transform: uppercase;
        }

        /* Visual Result Card */
        .visual-card {
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            padding: 8px;
            text-align: center;
            box-shadow: 0 4px 16px -4px rgba(0, 0, 0, 0.05);
            margin-bottom: 6px;
            transition: all 0.2s ease;
        }
        .visual-card:hover {
            transform: translateY(-2px);
            border-color: #c7d2fe;
            box-shadow: 0 8px 24px -6px rgba(99, 102, 241, 0.15);
        }
        .card-label {
            font-size: 0.75rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            color: #475569;
            margin-bottom: 6px;
            padding-bottom: 3px;
            border-bottom: 1px solid #f1f5f9;
        }

        /* Safe File Uploader (No Text Collision) */
        [data-testid="stFileUploader"] {
            margin-bottom: 8px;
        }
        [data-testid="stFileUploader"] section {
            background: rgba(255, 255, 255, 0.7) !important;
            border: 1.5px dashed #c7d2fe !important;
            border-radius: 10px !important;
            padding: 12px 14px !important;
        }
        [data-testid="stFileUploader"] button {
            background: #4f46e5 !important;
            color: #ffffff !important;
            border-radius: 6px !important;
            border: none !important;
            font-size: 0.78rem !important;
            font-weight: 600 !important;
            padding: 4px 12px !important;
            box-shadow: 0 2px 6px rgba(79, 70, 229, 0.25) !important;
        }
        [data-testid="stFileUploader"] button:hover {
            background: #4338ca !important;
        }
        [data-testid="stFileUploader"] small {
            font-size: 0.75rem !important;
            color: #64748b !important;
        }

        /* Image Display Bounds */
        img {
            max-height: 200px !important;
            object-fit: contain !important;
            border-radius: 6px;
        }

        /* Download Button */
        div.stDownloadButton > button {
            background: #f8fafc;
            color: #4f46e5;
            border: 1px solid #c7d2fe;
            border-radius: 6px;
            font-size: 0.74rem;
            font-weight: 700;
            padding: 3px 8px;
            margin-top: 3px;
            transition: all 0.2s ease;
        }
        div.stDownloadButton > button:hover {
            background: #4f46e5;
            color: #ffffff;
            border-color: #4f46e5;
            box-shadow: 0 4px 12px rgba(79, 70, 229, 0.25);
        }

        .metric-badge {
            display: inline-block;
            background: #ede9fe;
            color: #4338ca;
            border: 1px solid #c7d2fe;
            padding: 3px 10px;
            border-radius: 12px;
            font-size: 0.78rem;
            font-weight: 700;
            margin: 2px 4px 6px 0;
        }
    </style>

    <div class="hero-banner">
        <div>
            <h1 class="main-title">Image Processing</h1>
            <div class="sub-title">Interactive Virtual Laboratory & Algorithm Studio</div>
        </div>
        <div style="background: rgba(99, 102, 241, 0.2); border: 1px solid rgba(129, 140, 248, 0.3); border-radius: 8px; padding: 6px 12px; color: #a5b4fc; font-size: 0.8rem; font-weight: 700;">
            PRO LAB SUITE
        </div>
    </div>
""",
    unsafe_allow_html=True,
)

# Sidebar Selection
selected_op = st.sidebar.selectbox(
    "Select Experiment:",
    [
        "01. Color Formats & Arithmetic",
        "02. 2-D Geometric Transformations",
        "03. Enhancement & Thresholding",
        "04. Spatial Domain Smoothing",
        "05. Image Inpainting & Restoration",
        "06. Lossless & Lossy Compression",
        "07. Morphological Operations",
        "08. Correlation-based Detection",
        "09. Advanced Color Spaces",
        "10. Multi-Operator Edge Detection",
    ],
)


def read_img(file):
    if file:
        return cv2.imdecode(
            np.asarray(bytearray(file.read()), dtype=np.uint8),
            cv2.IMREAD_COLOR,
        )
    return None


def render_card(title, image, is_gray=False, key="d"):
    st.markdown(
        f'<div class="visual-card"><div class="card-label">{title}</div>',
        unsafe_allow_html=True,
    )
    if is_gray:
        st.image(image, channels="GRAY", use_container_width=True)
        _, buf = cv2.imencode(".png", image)
    else:
        st.image(
            cv2.cvtColor(image, cv2.COLOR_BGR2RGB), use_container_width=True
        )
        _, buf = cv2.imencode(".png", image)
    st.markdown("</div>", unsafe_allow_html=True)
    st.download_button(
        label=f"⬇️ Download {title}",
        data=buf.tobytes(),
        file_name=f"{title.lower().replace(' ', '_')}.png",
        mime="image/png",
        key=f"dl_{key}",
        use_container_width=True,
    )


# =========================================================
# 01. Color Formats & Arithmetic
# =========================================================
if selected_op.startswith("01."):
    st.markdown(
        """
        <div class="aim-card">
            <span class="aim-tag">Aim</span>
            To convert images between various formats like RGB and Grayscale, perform arithmetic and bitwise operations on the images, and observe how these operations affect the image data representation.
        </div>
    """,
        unsafe_allow_html=True,
    )

    col_l, col_r = st.columns([1.1, 2.5])
    with col_l:
        sub = st.selectbox(
            "Sub-operation Mode:",
            [
                "Color Format Conversion",
                "Arithmetic: Weighted Blend",
                "Arithmetic: Subtraction",
                "Bitwise Operations",
            ],
        )
        if sub == "Color Format Conversion":
            u = st.file_uploader(
                "Upload Image:", type=["jpg", "jpeg", "png"], key="p2_u"
            )
        else:
            u1 = st.file_uploader("Primary Image:", type=["jpg", "png"], key="p2_1")
            u2 = st.file_uploader("Secondary Image:", type=["jpg", "png"], key="p2_2")

    with col_r:
        if sub == "Color Format Conversion" and "u" in locals() and u:
            img = read_img(u)
            c1, c2, c3 = st.columns(3)
            with c1:
                render_card("Raw BGR as RGB", img, key="p2_raw")
            with c2:
                render_card("Standard RGB", img, key="p2_rgb")
            with c3:
                render_card(
                    "Grayscale",
                    cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
                    is_gray=True,
                    key="p2_gray",
                )
        elif sub != "Color Format Conversion" and "u1" in locals() and u1 and u2:
            i1, i2 = read_img(u1), read_img(u2)
            i2 = cv2.resize(i2, (i1.shape[1], i1.shape[0]))
            if sub == "Arithmetic: Weighted Blend":
                w = st.slider("Blend Factor", 0.0, 1.0, 0.5)
                res = cv2.addWeighted(i1, w, i2, 1.0 - w, 0)
                render_card("Weighted Blend Result", res, key="p2_bld")
            elif sub == "Arithmetic: Subtraction":
                render_card("Subtracted Result", cv2.subtract(i1, i2), key="p2_sub")
            else:
                b_op = st.radio(
                    "Logic:", ["AND", "OR", "XOR", "NOT"], horizontal=True
                )
                ops = {
                    "AND": cv2.bitwise_and(i1, i2),
                    "OR": cv2.bitwise_or(i1, i2),
                    "XOR": cv2.bitwise_xor(i1, i2),
                    "NOT": cv2.bitwise_not(i1),
                }
                render_card(f"Bitwise {b_op}", ops[b_op], key="p2_bit")

# =========================================================
# 02. 2-D Geometric Transformations
# =========================================================
elif selected_op.startswith("02."):
    st.markdown(
        """
        <div class="aim-card">
            <span class="aim-tag">Aim</span>
            Develop programs to apply the following 2-D geometric transformation operations on an image: i) Translation ii) Rotation iii) Scaling iv) Shearing v) Reflection and vi) Cropping.
        </div>
    """,
        unsafe_allow_html=True,
    )

    col_l, col_r = st.columns([1.1, 2.2])
    with col_l:
        op = st.selectbox(
            "Transformation:",
            [
                "Translation",
                "Rotation",
                "Scaling",
                "Shearing X",
                "Shearing Y",
                "Reflection",
                "Cropping",
            ],
        )
        u = st.file_uploader("Upload Image:", type=["jpg", "png"], key="p3_u")
    if u:
        img = read_img(u)
        h, w = img.shape[:2]
        with col_l:
            if op == "Translation":
                tx = st.slider("Translate X (px)", -w, w, 50)
                ty = st.slider("Translate Y (px)", -h, h, 30)
                res = cv2.warpAffine(
                    img, np.float32([[1, 0, tx], [0, 1, ty]]), (w, h)
                )
            elif op == "Rotation":
                a = st.slider("Angle (°)", -180, 180, 30)
                s = st.slider("Scale", 0.3, 2.0, 0.8)
                res = cv2.warpAffine(
                    img, cv2.getRotationMatrix2D((w / 2, h / 2), a, s), (w, h)
                )
            elif op == "Scaling":
                f = st.slider("Multiplier", 0.3, 2.5, 1.2)
                res = cv2.resize(img, None, fx=f, fy=f)
            elif op == "Shearing X":
                s = st.slider("Shear X", 0.0, 1.5, 0.5)
                res = cv2.warpPerspective(
                    img,
                    np.float32([[1, s, 0], [0, 1, 0], [0, 0, 1]]),
                    (int(w * 1.3), int(h * 1.3)),
                )
            elif op == "Shearing Y":
                s = st.slider("Shear Y", 0.0, 1.5, 0.5)
                res = cv2.warpPerspective(
                    img,
                    np.float32([[1, 0, 0], [s, 1, 0], [0, 0, 1]]),
                    (int(w * 1.3), int(h * 1.3)),
                )
            elif op == "Reflection":
                fl = st.selectbox(
                    "Axis:", [("Vertical", 0), ("Horizontal", 1), ("Both", -1)]
                )
                res = cv2.flip(img, fl[1])
            elif op == "Cropping":
                y1, y2 = st.slider("Y Range", 0, h, (0, min(h, 180)))
                x1, x2 = st.slider("X Range", 0, w, (0, min(w, 180)))
                res = img[y1:y2, x1:x2]
        with col_r:
            c1, c2 = st.columns(2)
            with c1:
                render_card("Original", img, key="p3_orig")
            with c2:
                render_card(f"Result ({op})", res, key="p3_res")

# =========================================================
# 03. Enhancement & Thresholding
# =========================================================
elif selected_op.startswith("03."):
    st.markdown(
        """
        <div class="aim-card">
            <span class="aim-tag">Aim</span>
            To study and implement image enhancement techniques in the spatial domain, including Histogram Equalization for contrast improvement, Spatial Filtering methods such as Smoothing and Sharpening to reduce noise and enhance important features, and Thresholding techniques to segment grayscale images based on pixel intensity.
        </div>
    """,
        unsafe_allow_html=True,
    )

    col_l, col_r = st.columns([1.1, 2.2])
    with col_l:
        op = st.selectbox(
            "Operation:",
            [
                "Negative Image",
                "Brightness & Contrast",
                "Sharpening Filter",
                "Histogram Equalization",
                "Thresholding",
            ],
        )
        u = st.file_uploader("Upload Image:", type=["jpg", "png"], key="p4_u")
    if u:
        img = read_img(u)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        with col_l:
            if op == "Negative Image":
                res, is_g = 255 - img, False
            elif op == "Brightness & Contrast":
                a = st.slider("Contrast Alpha", 0.5, 3.0, 1.4)
                b = st.slider("Brightness Beta", -100, 100, 25)
                res, is_g = cv2.convertScaleAbs(img, alpha=a, beta=b), False
            elif op == "Sharpening Filter":
                k = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
                res, is_g = cv2.filter2D(img, -1, k), False
            elif op == "Histogram Equalization":
                res, is_g = cv2.equalizeHist(gray), True
            elif op == "Thresholding":
                t_val = st.slider("Threshold Boundary", 0, 255, 127)
                t_type = st.selectbox(
                    "Mode:",
                    [
                        "THRESH_BINARY",
                        "THRESH_BINARY_INV",
                        "THRESH_TRUNC",
                        "THRESH_TOZERO",
                    ],
                )
                _, res = cv2.threshold(gray, t_val, 255, getattr(cv2, t_type))
                is_g = True
        with col_r:
            c1, c2 = st.columns(2)
            with c1:
                render_card(
                    "Source", gray if is_g else img, is_gray=is_g, key="p4_src"
                )
            with c2:
                render_card("Enhanced Result", res, is_gray=is_g, key="p4_res")

# =========================================================
# 04. Spatial Domain Smoothing
# =========================================================
elif selected_op.startswith("04."):
    st.markdown(
        """
        <div class="aim-card">
            <span class="aim-tag">Aim</span>
            To write Python programs using OpenCV to apply different spatial domain filters on a given image, including: i. Averaging Filter ii. Gaussian Filter iii. Median Filter iv. Bilateral Filter.
        </div>
    """,
        unsafe_allow_html=True,
    )

    col_l, col_r = st.columns([1.1, 2.2])
    with col_l:
        f_type = st.selectbox(
            "Filter Kernel:", ["Averaging", "Gaussian", "Median", "Bilateral"]
        )
        u = st.file_uploader("Upload Image:", type=["jpg", "png"], key="p5_u")
        k = st.slider("Kernel Size (Odd)", 3, 21, 5, step=2)
    if u:
        img = read_img(u)
        if f_type == "Averaging":
            res = cv2.blur(img, (k, k))
        elif f_type == "Gaussian":
            res = cv2.GaussianBlur(img, (k, k), 1.0)
        elif f_type == "Median":
            res = cv2.medianBlur(img, k)
        else:
            res = cv2.bilateralFilter(img, k, 75, 75)
        with col_r:
            c1, c2 = st.columns(2)
            with c1:
                render_card("Source Image", img, key="p5_src")
            with c2:
                render_card(f"Filtered ({f_type})", res, key="p5_out")

# =========================================================
# 05. Image Inpainting & Restoration
# =========================================================
elif selected_op.startswith("05."):
    st.markdown(
        """
        <div class="aim-card">
            <span class="aim-tag">Aim</span>
            Implement to remove damaged parts of an image using inpainting methods. The experiment uses two approaches – Telea method and Navier-Stokes (NS) method – to restore the image and make it look natural.
        </div>
    """,
        unsafe_allow_html=True,
    )

    col_l, col_r = st.columns([1.1, 2.6])
    with col_l:
        u = st.file_uploader("Upload Image:", type=["jpg", "png"], key="p6_u")
        use_sample = st.checkbox("Generate Test Scratches")
        method = st.radio("Algorithm:", ["Telea", "Navier-Stokes"], horizontal=True)
        rad = st.slider("Inpaint Radius", 1, 8, 3)
    if u:
        img = read_img(u)
        if use_sample:
            cv2.line(
                img,
                (15, 20),
                (img.shape[1] - 20, img.shape[0] - 20),
                (255, 255, 255),
                3,
            )
            cv2.circle(
                img,
                (img.shape[1] // 2, img.shape[0] // 2),
                22,
                (255, 255, 255),
                -1,
            )
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, mask = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
        flag = cv2.INPAINT_TELEA if method == "Telea" else cv2.INPAINT_NS
        restored = cv2.inpaint(img, mask, rad, flag)
        with col_r:
            c1, c2, c3 = st.columns(3)
            with c1:
                render_card("Damaged Input", img, key="p6_dam")
            with c2:
                render_card("Defect Mask", mask, is_gray=True, key="p6_mask")
            with c3:
                render_card(f"Restored ({method})", restored, key="p6_res")

# =========================================================
# 06. Lossless & Lossy Compression
# =========================================================
elif selected_op.startswith("06."):
    st.markdown(
        """
        <div class="aim-card">
            <span class="aim-tag">Aim</span>
            Implement a coding technique to achieve lossless compression and compare the original and compressed file sizes.
        </div>
    """,
        unsafe_allow_html=True,
    )

    col_l, col_r = st.columns([1.1, 2.2])
    with col_l:
        u = st.file_uploader("Upload Image:", type=["jpg", "png"], key="p7_u")
        q = st.slider("JPEG Quality Factor", 5, 100, 30)
    if u:
        img = read_img(u)
        with tempfile.TemporaryDirectory() as td:
            p0, pj, pp = (
                os.path.join(td, "o.jpg"),
                os.path.join(td, "j.jpg"),
                os.path.join(td, "p.png"),
            )
            cv2.imwrite(p0, img)
            cv2.imwrite(pj, img, [cv2.IMWRITE_JPEG_QUALITY, q])
            cv2.imwrite(pp, img, [cv2.IMWRITE_PNG_COMPRESSION, 9])
            s0, sj, sp = (
                os.path.getsize(p0) / 1024,
                os.path.getsize(pj) / 1024,
                os.path.getsize(pp) / 1024,
            )
            with col_l:
                st.markdown(
                    f"""
                    <div style="margin-top: 6px;">
                        <span class="metric-badge">Orig: {s0:.1f} KB</span>
                        <span class="metric-badge">JPEG: {sj:.1f} KB ({s0 / sj:.1f}:1)</span>
                        <span class="metric-badge">PNG: {sp:.1f} KB ({s0 / sp:.1f}:1)</span>
                    </div>
                """,
                    unsafe_allow_html=True,
                )
            with col_r:
                c1, c2 = st.columns(2)
                with c1:
                    render_card("Original", img, key="p7_orig")
                with c2:
                    render_card(
                        "Compressed JPEG", cv2.imread(pj), key="p7_comp"
                    )

# =========================================================
# 07. Morphological Operations
# =========================================================
elif selected_op.startswith("07."):
    st.markdown(
        """
        <div class="aim-card">
            <span class="aim-tag">Aim</span>
            Perform morphological operations erosion, dilation, opening, and closing on binary images to study their effects on object shapes and noise removal.
        </div>
    """,
        unsafe_allow_html=True,
    )

    col_l, col_r = st.columns([1.1, 2.2])
    with col_l:
        m_op = st.selectbox(
            "Operation:", ["Erosion", "Dilation", "Opening", "Closing"]
        )
        k_dim = st.slider("Structuring Element Size", 3, 21, 5, step=2)
        u = st.file_uploader("Upload Image:", type=["jpg", "png"], key="p8_u")
    if u:
        img = read_img(u)
        _, binary = cv2.threshold(
            cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 127, 255, cv2.THRESH_BINARY
        )
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (k_dim, k_dim))
        ops = {
            "Erosion": cv2.erode(binary, kernel),
            "Dilation": cv2.dilate(binary, kernel),
            "Opening": cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel),
            "Closing": cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel),
        }
        with col_r:
            c1, c2 = st.columns(2)
            with c1:
                render_card("Binary Input", binary, is_gray=True, key="p8_bin")
            with c2:
                render_card(
                    f"Result: {m_op}", ops[m_op], is_gray=True, key="p8_out"
                )

# =========================================================
# 08. Correlation-based Detection
# =========================================================
elif selected_op.startswith("08."):
    st.markdown(
        """
        <div class="aim-card">
            <span class="aim-tag">Aim</span>
            Develop a program to detect object using the correlation principle.
        </div>
    """,
        unsafe_allow_html=True,
    )

    col_l, col_r = st.columns([1.1, 2.2])
    with col_l:
        u_main = st.file_uploader(
            "Upload Scene Image:", type=["jpg", "png"], key="p9_m"
        )
        u_temp = st.file_uploader(
            "Upload Template Target:", type=["jpg", "png"], key="p9_t"
        )
        thresh = st.slider("Correlation Threshold", 0.1, 1.0, 0.8)

    if u_main and u_temp:
        im, temp = read_img(u_main), read_img(u_temp)
        th, tw = temp.shape[:2]
        corr = cv2.matchTemplate(
            cv2.cvtColor(im, cv2.COLOR_BGR2GRAY),
            cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY),
            cv2.TM_CCOEFF_NORMED,
        )
        loc = np.where(corr >= thresh)
        res_im = im.copy()
        hits = 0
        for pt in zip(*loc[::-1]):
            cv2.rectangle(res_im, pt, (pt[0] + tw, pt[1] + th), (0, 255, 0), 2)
            hits += 1

        with col_r:
            c_a, c_b = st.columns(2)
            with c_a:
                render_card("Target Template", temp, key="p9_tmp")
            with c_b:
                render_card(
                    f"Matches Detected ({hits})", res_im, key="p9_res"
                )

# =========================================================
# 09. Advanced Color Spaces
# =========================================================
elif selected_op.startswith("09."):
    st.markdown(
        """
        <div class="aim-card">
            <span class="aim-tag">Aim</span>
            Convert images between the RGB, HSV, YCrCb, and Lab colour spaces, analyzing how colour information is encoded in each.
        </div>
    """,
        unsafe_allow_html=True,
    )

    col_l, col_r = st.columns([1.1, 2.8])
    with col_l:
        u = st.file_uploader("Upload Image:", type=["jpg", "png"], key="pl2_u")
        view = st.radio("Display Mode:", ["Full Spaces", "Channel Split"])
    if u:
        img = read_img(u)
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
        lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

        with col_r:
            if view == "Full Spaces":
                c1, c2, c3, c4 = st.columns(4)
                with c1:
                    render_card("RGB", rgb, key="pl2_rgb")
                with c2:
                    render_card("HSV", hsv, key="pl2_hsv")
                with c3:
                    render_card("YCrCb", ycrcb, key="pl2_ycrcb")
                with c4:
                    render_card("CIE-Lab", lab, key="pl2_lab")
            else:
                space = st.selectbox(
                    "Color Space:", ["RGB", "HSV", "YCrCb", "Lab"]
                )
                c1, c2, c3 = st.columns(3)
                if space == "RGB":
                    r, g, b = cv2.split(rgb)
                    with c1:
                        render_card("Red", r, is_gray=True, key="pl2_r")
                    with c2:
                        render_card("Green", g, is_gray=True, key="pl2_g")
                    with c3:
                        render_card("Blue", b, is_gray=True, key="pl2_b")
                elif space == "HSV":
                    h, s, v = cv2.split(hsv)
                    with c1:
                        render_card("Hue", h, is_gray=True, key="pl2_h")
                    with c2:
                        render_card(
                            "Saturation", s, is_gray=True, key="pl2_s"
                        )
                    with c3:
                        render_card("Value", v, is_gray=True, key="pl2_v")
                elif space == "YCrCb":
                    y, cr, cb = cv2.split(ycrcb)
                    with c1:
                        render_card("Y (Luma)", y, is_gray=True, key="pl2_y")
                    with c2:
                        render_card(
                            "Cr (Chroma Red)", cr, is_gray=True, key="pl2_cr"
                        )
                    with c3:
                        render_card(
                            "Cb (Chroma Blue)", cb, is_gray=True, key="pl2_cb"
                        )
                elif space == "Lab":
                    l, a, b = cv2.split(lab)
                    with c1:
                        render_card(
                            "L (Lightness)", l, is_gray=True, key="pl2_l"
                        )
                    with c2:
                        render_card(
                            "a* (Green-Red)", a, is_gray=True, key="pl2_a"
                        )
                    with c3:
                        render_card(
                            "b* (Blue-Yellow)", b, is_gray=True, key="pl2_b"
                        )

# =========================================================
# 10. Multi-Operator Edge Detection
# =========================================================
elif selected_op.startswith("10."):
    st.markdown(
        """
        <div class="aim-card">
            <span class="aim-tag">Aim</span>
            Detect edges in images with the Canny method and contrast the results with Sobel and Prewitt detectors.
        </div>
    """,
        unsafe_allow_html=True,
    )

    col_l, col_r = st.columns([1.1, 2.8])
    with col_l:
        u = st.file_uploader("Upload Image:", type=["jpg", "png"], key="pl3_u")
        t_low = st.slider("Canny Low Threshold", 10, 200, 50)
        t_high = st.slider("Canny High Threshold", 50, 300, 150)
        k_blur = st.slider("Gaussian Blur Kernel", 1, 9, 3, step=2)

    if u:
        img = read_img(u)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (k_blur, k_blur), 1.2)

        # Canny
        canny = cv2.Canny(blurred, t_low, t_high)

        # Sobel
        sx = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=3)
        sy = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)
        sobel = np.uint8(cv2.magnitude(sx, sy))

        # Prewitt
        kx = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=np.float32)
        ky = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]], dtype=np.float32)
        px = cv2.filter2D(blurred, cv2.CV_64F, kx)
        py = cv2.filter2D(blurred, cv2.CV_64F, ky)
        prewitt = np.uint8(cv2.magnitude(px, py))

        with col_r:
            c1, c2, c3, c4 = st.columns(4)
            with c1:
                render_card("Original", img, key="pl3_orig")
            with c2:
                render_card(
                    "Canny Edges", canny, is_gray=True, key="pl3_canny"
                )
            with c3:
                render_card(
                    "Sobel Edges", sobel, is_gray=True, key="pl3_sobel"
                )
            with c4:
                render_card(
                    "Prewitt Edges", prewitt, is_gray=True, key="pl3_prew"
                )